import os
import io
import uvicorn
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from fastapi import FastAPI, Response

# 1. Use non-interactive backend
matplotlib.use('Agg')

app = FastAPI()

@app.get("/")
def generate_plot():
    # Clear previous plot
    plt.clf()
    
    # 2. Identify configuration
    plot_type = os.environ.get('PLOT_TYPE', 'bar')
    container_id = os.environ.get('HOSTNAME', 'unknown-container')

    # 3. Generate Data
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
    
    # 4. Create Plot
    sns.set_theme(style="whitegrid")
    
    if plot_type == 'box':
        title = f"[Box Service] ID: {container_id}"
        sns.boxplot(data=df)
    elif plot_type == 'hist':
        title = f"[Hist Service] ID: {container_id}"
        sns.histplot(data=df, kde=True)
    else:
        summary = df.sum().reset_index()
        summary.columns = ['Category', 'Value']
        title = f"[Bar Service] ID: {container_id}"
        sns.barplot(data=summary, x='Category', y='Value')

    plt.title(title)
    
    # 5. Save to memory buffer
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    
    # 6. Return raw bytes with correct MIME type
    return Response(content=img.getvalue(), media_type="image/png")

if __name__ == '__main__':
    # Run using Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)