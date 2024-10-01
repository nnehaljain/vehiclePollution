import tkinter as ttk
import pandas as pd

model = pd.read_pickle(r"C:\Users\Admin\Downloads\co2Emmisions\co2emission.pkl")


app = ttk.Tk()
app.geometry('300x300')
app.title('CO2 Emission Predictor')

engine_size = ttk.Variable(app)
ttk.Label(app, text = 'Engine Size', padx=15, pady=15).grid(row=0, column=0)
ttk.Entry(app, textvariable=engine_size, width=10).grid(row=0, column=1)

cylinders = ttk.Variable(app)
ttk.Label(app, text = 'No. of Cylinders', padx=15, pady=15).grid(row=1, column=0)
ttk.Entry(app, textvariable=cylinders, width=10).grid(row=1, column=1)

mileage = ttk.Variable(app)
ttk.Label(app, text = 'Mileage of Car', padx=15, pady=15).grid(row=2, column=0)
ttk.Entry(app, textvariable=mileage, width=10).grid(row=2, column=1)

def prediction():
    global model
    query_data = {
        'ENGINESIZE':[eval(engine_size.get())],
        'CYLINDERS':[eval(cylinders.get())],
        'FUELCONSUMPTION_COMB':[eval(mileage.get())]}
    price = model.predict(pd.DataFrame(query_data))
    result.set(round(price[0], 2))

ttk.Button(app, text='Predict!', command=prediction).grid(row=4, column=0, columnspan=2)

result = ttk.Variable(app)
result.set('0')
ttk.Label(app, textvariable=result, pady=15, font = ('Arial', 20)).grid(row=5, column=0, columnspan=2)

app.mainloop()
