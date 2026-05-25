"""
Main server for emotion detection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")


@app.route("/emotionDetector")
def detecting_emotions():
    """Show the result for emotion detection."""

    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again."

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is "
        f"{result['dominant_emotion']}."
    )


@app.route("/")
def render_index():
    """Render the index page for emotion detection."""

    return render_template("index.html")


if __name__ == "__main__":
    #Execute the Flask app and deploy it on localhost:5000.

    app.run(host="0.0.0.0", port=5000)
