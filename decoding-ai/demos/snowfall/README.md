# Interactive Snowfall Predictor Map

This was an experiment to see if an AI model could generate a snowfall prediction map application. It was entered into a variety of Chatbots including https://huggingface.co/spaces/akhaliq/anychat.

Numerous prompts were tried, but the AI model struggled to generate a fully functional application. You can open the html files in this folder with your browser to see the variations of the generated apps.

## Lessons Learned

- When generating code, it's important to set your expectations right.
- Single purpose applications create impressive demos, but practical applications require more complex logic and will need a bit more design work.
- Provide a clear and detailed prompt to the AI model to get the desired output. It will often require multiple iterations to refine the prompt to get the desired output.
- Sometimes it's better to step back and break down the problem into smaller parts.
- If you have a preferred framework or technology stack, it's also helpful to mention that in the prompt to guide the AI model in generating the code.
- You can also ask the AI to generate a prompt, which helps provide a structured format. You can then refine as needed.

## Prompt Example 1

```text
Create  a browser based app that shows a map of my current location with  a color coded overlay of predicted snowfall over the next week.  Provide a time slider to show updated predictions in 8 hour windows. 
```

## Prompt Example 2

```text
Create  a browser based app that shows a map of location with a zip code entry box (default 48895) with  a color coded overlay of predicted snowfall over the 7 days using a reliable public API of predicted weather data.  Provide a time slider to show updated predictions in 12 hour windows. 
```

## Prompt Example 3

```text
Create  a browser based app that shows a map centered on a zip code entered in an input box (default 48895). The visible map area will have an overlay grid with an overlay indicating predicted cumulative snowfall between the begin time and end time selected by a time slider. The range of the time slider will be the current time (ts) to maximum time (tmax = ts + 7 days). Prediction data should come from a reliable public API.
```
## Output

```text
Certainly! Here's a prompt for an AI model to recreate the snowfall prediction map application:

---

Create a web application that displays a map showing predicted snowfall for a given ZIP code in the United States. The application should have the following features and specifications:

1. User Interface:
   - An input field for entering a ZIP code (default value: 48895)
   - A "Update Location” button to recenter the map on the location in the Zip code input field
   - A map display area
   

2. Map Functionality:
   - Use Leaflet.js for map rendering
   - Initially center the map on ZIP code 48895
   - Use OpenStreetMap tiles for the base map

3. Data Retrieval:
   - Use the Nominatim API to convert ZIP codes to latitude and longitude
   - Use the Open-Meteo API to fetch snowfall prediction data
   - No API key should be required for these services

4. Snowfall Visualization:
     - A pointer that when clicked, pops up a 7 day bar chart of predicted snowfall for the clicked location.
     - Allow multiple pop up bar charts that can be closed individually.

5. Dynamic Updates:
   - Update the map and snowfall overlay when a new ZIP code is entered

6. Error Handling:
   - Display an alert if an invalid ZIP code is entered or if data fetching fails

7. Code Structure:
   - Use HTML for structure, inline CSS for styling, and JavaScript for functionality
   - Implement as a single, self-contained HTML file
   - Ensure compatibility with modern web browsers

8. Additional Requirements:
   - The application should be responsive and work on both desktop and mobile devices
   - Include comments in the code to explain key functionalities
   - Optimize for performance, especially when fetching and updating data

Provide the complete HTML code for this application, including all necessary JavaScript and CSS. Ensure that the code is well-structured, efficient, and follows best practices for web development.
```