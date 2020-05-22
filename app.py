from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def plot():
    from pandas_datareader import data, wb
    import datetime
    from bokeh.plotting import figure, show, output_file
    from bokeh.io import output_notebook

    start_date = datetime.datetime(2019,12,1)
    end_date = datetime.datetime(2020,5,20)

    df = data.DataReader(name="GOOG", data_source="yahoo", start=start_date, end=end_date)

    def inc_dec(c, o):
        if c > o:
            value="Increase"
        elif c < o:
            value="Decrease"
        else:
            value="Equal"
        return value
        
    df["Status"]=[inc_dec(c,o) for c, o in zip(df.Close,df.Open)]
    df["Middle"]=(df.Open+df.Close)/2
    df["Height"]=abs(df.Close-df.Open)

    # df

    p = figure(x_axis_type="datetime", width=500, height=250, sizing_mode='stretch_both', title="Candlestick Chart")
    p.grid.grid_line_alpha=0.3

    hours_12 = 12*60*60*1000

    p.segment(df.index, df.High, df.index, df.Low, color="Black")

    p.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"],
           hours_12, df.Height[df.Status=="Increase"],fill_color="green",line_color="black")

    p.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"],
           hours_12, df.Height[df.Status=="Decrease"],fill_color="red",line_color="black")


    return render_template("plot2.html")


if __name__=="__main__":
    app.run(debug=True)
