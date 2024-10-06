import React, {useState, useEffect} from 'react';
import { useLocation } from 'react-router-dom';
import axios from 'axios';

function Output(
//   { prompt = "Sample Prompt", date = "2023-01-01", stock = "S&P 500", result = { trend: "increase", decrease: 10, neutral: 20, increase: 70 }, themes = [
//   { title: "Economic Growth", description: "Economic growth is a key driver of stock market performance. When the economy is growing, businesses tend to perform better, leading to higher stock prices. Investors are more confident in the market, and there is generally more liquidity. This theme explores the various factors that contribute to economic growth, such as consumer spending, business investment, government policies, and global trade." },
//   { title: "Technological Innovation", description: "Technological innovation has a profound impact on the stock market. Companies that are at the forefront of technological advancements often see significant growth in their stock prices. This theme delves into the latest technological trends, such as artificial intelligence, blockchain, and renewable energy, and how they are shaping the future of industries and the stock market. It also examines the risks and opportunities associated with investing in tech-driven companies." },
//   { title: "Geopolitical Events", description: "Geopolitical events can have a major influence on the stock market. Events such as elections, trade wars, and international conflicts can create uncertainty and volatility in the market. This theme analyzes the potential impact of various geopolitical events on different sectors and stocks. It also provides insights into how investors can navigate the complexities of geopolitics to make informed investment decisions." }
// ], sources = [{ name: "Sample Source", rationale: "Sample Rationale", categories: ["Cat1", "Cat2"] }] }
) {

    const location = useLocation();
    // const { searchValue, selectedStock, selectedDate } = location.state;
    // const [data, setData] = useState({
    //   prompt: searchValue,
    //   date: selectedDate,
    //   stock: selectedStock,
    //   result: { trend: "", decrease: 0, neutral: 0, increase: 0 },
    //   themes: [],
    //   sources: []
    // });

    useEffect(() => {
        try {
            axios.get('http://crystalball.onrender.com/') // UPDATE THIS LATER AND FIGURE OUT SCHEMA
            .then((res) => {
                console.log(res.data);
                setDate(res.data);
            })
        } catch (error) {
            console.log(error);
        }
    }, []);


    const resultJSON = `{
            "market_prediction": "NEUTRAL",
            "buy_percentage": 10,
            "sell_percentage": 20,
            "hold_percentage": 70,
            "weighted_buy_probability": 0.2,
            "weighted_sell_probability": 0.5,
            "summary": "This is an explanation of what happened"
            }`

    const stock = "S&P 500"
    const prompt = "taylor announces a new tour"
    const date = "2024-05-01"
    const result = JSON.parse(resultJSON);

    const themes_result_sell = { 
        "Personas": "Investor/Institution Name",
        "title": "A short title for this summary",
        "description": "A description"
    }
    const themes_result_buy= { 
        "Personas": "Investor/Institution Name",
        "title": "A short title for this summary",
        "description": "A description"
    }
    const themes_result_hold= { 
        "Personas": "Investor/Institution Name",
        "title": "A short title for this summary",
        "description": "A description"
    }

    const themes = [
        { title: "Economic Growth", description: "Economic growth is a key driver of stock market performance. When the economy is growing, businesses tend to perform better, leading to higher stock prices. Investors are more confident in the market, and there is generally more liquidity. This theme explores the various factors that contribute to economic growth, such as consumer spending, business investment, government policies, and global trade." },
        { title: "Technological Innovation", description: "Technological innovation has a profound impact on the stock market. Companies that are at the forefront of technological advancements often see significant growth in their stock prices. This theme delves into the latest technological trends, such as artificial intelligence, blockchain, and renewable energy, and how they are shaping the future of industries and the stock market. It also examines the risks and opportunities associated with investing in tech-driven companies." },
        { title: "Geopolitical Events", description: "Geopolitical events can have a major influence on the stock market. Events such as elections, trade wars, and international conflicts can create uncertainty and volatility in the market. This theme analyzes the potential impact of various geopolitical events on different sectors and stocks. It also provides insights into how investors can navigate the complexities of geopolitics to make informed investment decisions." }
    ]
    const sources = [
        { name: "Sample Source", rationale: "Sample Rationale", categories: ["Cat1", "Cat2"] }
    ] 

  
  
    return (
    <div className="flex flex-col items-center justify-start min-h-screen pt-20">
      <div className="w-full max-w-4xl">
        <div className="flex flex-col items-start mb-6">
          <h1 className="text-2xl font-bold mb-3">{stock} impact if {prompt}</h1>
          <div className="flex flex-wrap gap-2 mb-3">
            <span className="text-gray-500 text-sm">{date}</span>
          </div>
        </div>

        <div className="mb-8 border border-gray-300 rounded-lg shadow-sm bg-white p-6">
          {/* <h2 className="text-xl font-semibold mb-2 text-left">Result</h2> */}
          <p className="text-4xl mt-4 mb-6 text-left">
            Your stock is expected to <span className={result.market_prediction === 'BULLISH' ? 'text-green-500' : result.market_prediction === 'BEARISH' ? 'text-red-500' : 'text-gray-500'}>{result.market_prediction}</span> {result.market_prediction === 'BULLISH' ? '⬆️' : result.market_prediction === 'BEARISH' ? '⬇️' : ''}
          </p>
          <p className="text-left text-gray-500">{result.summary}</p>
          <div className="flex gap-2">
            <div className={`p-4 border border-gray-300 rounded-lg shadow-sm bg-red-100`} style={{ width: `${result.sell_percentage}%` }}></div>
            <div className={`p-4 border border-gray-300 rounded-lg shadow-sm bg-gray-100`} style={{ width: `${result.hold_percentage}%` }}></div>
            <div className={`p-4 border border-gray-300 rounded-lg shadow-sm bg-green-100`} style={{ width: `${result.buy_percentage}%` }}></div>
          </div>
          <div className="mt-6 flex">
            <div className="text-left mr-8">
              <p className="text-lg font-semibold text-gray-500">Sell</p>
              <p className="text-2xl">⬇️ {result.sell_percentage}%</p>
            </div>
            <div className="text-left mr-8">
              <p className="text-lg font-semibold text-gray-500">Hold</p>
              <p className="text-2xl">😐 {result.hold_percentage}%</p>
            </div>
            <div className="text-left">
              <p className="text-lg font-semibold text-gray-500">Buy</p>
              <p className="text-2xl">⬆️ {result.buy_percentage}%</p>
            </div>
          </div>
        </div>

        <div className="mb-8 ">
          <h2 className="text-2xl font-semibold mb-2 text-left">Investor Rationale</h2>
          <div className="mb-4">
            <h3 className="text-lg font-semibold text-left border-b border-gray-300 pt-2">Sell Themes</h3>
            <p className="text-left mt-2">{themes_result_sell.description}</p>
          </div>
          <div className="mb-4">
            <h3 className="text-lg font-semibold text-left border-b border-gray-300 pt-2">Buy Themes</h3>
            <p className="text-left mt-2">{themes_result_buy.description}</p>
          </div>
          <div className="mb-4">
            <h3 className="text-lg font-semibold text-left border-b border-gray-300 pt-2">Hold Themes</h3>
            <p className="text-left mt-2">{themes_result_hold.description}</p>
          </div>
        </div>

        <div className="mb-8">
          <h2 className="text-2xl font-semibold mb-2 text-left">Segment Summary</h2>
          <div className="flex overflow-x-scroll space-x-4">
            {themes.map((theme, index) => (
              <div key={index} className={`p-4 border border-gray-300 rounded-lg shadow-sm w-64 ${index % 2 === 0 ? 'bg-blue-100' : 'bg-green-100'}`}>
                <h3 className="text-lg font-semibold text-left">{theme.title}</h3>
                <p className="text-left">{theme.description}</p>
              </div>
            ))}
          </div>
        </div>

        <div className="mb-6">
          <h2 className="text-2xl font-semibold mb-2 text-left">Source Sample Set</h2>
          <p className="text-sm text-gray-500 mb-4 text-left">Showing 50/1000</p>
          {sources.map((source, index) => (
            <div key={index} className="p-4 border border-gray-300 rounded-lg shadow-sm mb-4 w-64">
              <h3 className="text-lg font-semibold text-left">{source.name}</h3>
              <p className="mb-2 text-left">{source.rationale}</p>
              <div className="flex flex-wrap">
                {source.categories.map((category, idx) => (
                  <span key={idx} className="px-2 py-1 bg-gray-200 rounded-full text-sm mr-2 mb-2">{category}</span>
                ))}
              </div>
            </div>
          ))}
        </div>

      </div>
    </div>
  );
}

export default Output;
