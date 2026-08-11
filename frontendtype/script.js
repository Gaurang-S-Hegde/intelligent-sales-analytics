async function predictChurn() {

    const customerData = {

        TotalSpent: Number(
            document.getElementById("TotalSpent").value
        ),

        TotalOrders: Number(
            document.getElementById("TotalOrders").value
        ),

        TotalQuantity: Number(
            document.getElementById("TotalQuantity").value
        ),

        AverageOrderValue: Number(
            document.getElementById("AverageOrderValue").value
        ),

        CustomerLifetime: Number(
            document.getElementById("CustomerLifetime").value
        ),

        Recency: Number(
            document.getElementById("Recency").value
        ),

        Frequency: Number(
            document.getElementById("Frequency").value
        )
    };


    try {

        const response = await fetch(
            "http://127.0.0.1:8000/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(customerData)
            }
        );


        if (!response.ok) {
            throw new Error("API request failed");
        }


        const result = await response.json();


        document.getElementById("prediction").textContent =
            result.churn_prediction === 1
                ? "Likely to Churn"
                : "Not Likely to Churn";


        document.getElementById("probability").textContent =
            (result.churn_probability * 100).toFixed(2) + "%";


        document.getElementById("risk").textContent =
            result.risk_level;


    } catch (error) {

        console.error(error);

        alert(
            "Could not connect to the prediction API. " +
            "Make sure FastAPI is running."
        );
    }
}