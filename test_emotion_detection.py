import unittest

from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        self.assertEqual(emotion_detector("I am glad this happened")['dominant_emotion'], 'Joy')
        self.assertEqual(emotion_detector("I am really mad about this")['dominant_emotion'], 'Anger')
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")['dominant_emotion'], 'Disgust')
        self.assertEqual(emotion_detector("I am so sad about this")['dominant_emotion'], 'Sadness')
        self.assertEqual(emotion_detector("I am really afraid that this will happen")['dominant_emotion'], 'Fear')

if __name__ == "__main__":
    unittest.main()