import React from 'react';

function Output({ prompt = "Sample Prompt", date = "2023-01-01", stock = "S&P 500", result = { trend: "increase", decrease: 10, neutral: 20, increase: 70 }, themes = [
  { title: "Economic Growth", description: "Economic growth is a key driver of stock market performance. When the economy is growing, businesses tend to perform better, leading to higher stock prices. Investors are more confident in the market, and there is generally more liquidity. This theme explores the various factors that contribute to economic growth, such as consumer spending, business investment, government policies, and global trade." },
  { title: "Technological Innovation", description: "Technological innovation has a profound impact on the stock market. Companies that are at the forefront of technological advancements often see significant growth in their stock prices. This theme delves into the latest technological trends, such as artificial intelligence, blockchain, and renewable energy, and how they are shaping the future of industries and the stock market. It also examines the risks and opportunities associated with investing in tech-driven companies." },
  { title: "Geopolitical Events", description: "Geopolitical events can have a major influence on the stock market. Events such as elections, trade wars, and international conflicts can create uncertainty and volatility in the market. This theme analyzes the potential impact of various geopolitical events on different sectors and stocks. It also provides insights into how investors can navigate the complexities of geopolitics to make informed investment decisions." }
], sources = [{ name: "Sample Source", rationale: "Sample Rationale", categories: ["Cat1", "Cat2"] }] }) {
    const decreasePercent = 0.2
    const neutralPercent = 0.3
    const increasePercent = 0.5
  
  
    return (
    <div className="flex flex-col items-center justify-start min-h-screen pt-20">
      <div className="w-full max-w-4xl">
        <div className="flex flex-col items-start mb-6">
          <h1 className="text-2xl font-bold mb-3">{stock} impact if {prompt}</h1>
          <div className="flex flex-wrap gap-2 mb-3">
            <span className="text-gray-500 text-sm">{date}</span>
          </div>
          <div className="flex flex-wrap gap-2 mb-3">
            <select className="p-2 border border-gray-300 rounded-full shadow-sm">
              <option value="">Category</option>
              {/* Add category options here */}
            </select>
            <select className="p-2 border border-gray-300 rounded-full shadow-sm">
              <option value="">Subcategory</option>
              {/* Add subcategory options here */}
            </select>
          </div>
        </div>

        <div className="mb-8 border border-gray-300 rounded-lg shadow-sm bg-white p-6">
          {/* <h2 className="text-xl font-semibold mb-2 text-left">Result</h2> */}
          <p className="text-4xl mt-4 mb-6 text-left">
            Your stock is expected to <span className={result.trend === 'increase' ? 'text-green-500' : 'text-red-500'}>{result.trend}</span> {result.trend === 'increase' ? '⬆️' : '⬇️'}
          </p>
          <div className="flex gap-2">
            <div className={`p-4 border border-gray-300 rounded-lg shadow-sm bg-red-100`} style={{ width: `${result.decrease}%` }}></div>
            <div className={`p-4 border border-gray-300 rounded-lg shadow-sm bg-gray-100`} style={{ width: `${result.neutral}%` }}></div>
            <div className={`p-4 border border-gray-300 rounded-lg shadow-sm bg-green-100`} style={{ width: `${result.increase}%` }}></div>
          </div>
          <div className="mt-6 flex">
            <div className="text-left mr-8">
              <p className="text-lg font-semibold text-gray-500">Decrease</p>
              <p className="text-2xl">⬇️ {result.decrease}%</p>
            </div>
            <div className="text-left mr-8">
              <p className="text-lg font-semibold text-gray-500">Neutral</p>
              <p className="text-2xl">😐 {result.neutral}%</p>
            </div>
            <div className="text-left">
              <p className="text-lg font-semibold text-gray-500">Increase</p>
              <p className="text-2xl">⬆️ {result.increase}%</p>
            </div>
          </div>
        </div>

        <div className="mb-8 ">
          <h2 className="text-2xl font-semibold mb-2 text-left">Investor Rationale</h2>
          {themes.map((theme, index) => (
            <div key={index} className="mb-4">
              <h3 className="text-lg font-semibold text-left border-b border-gray-300 pt-2">{theme.title}</h3>
              <p className="text-left mt-2">{theme.description}</p>
            </div>
          ))}
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
