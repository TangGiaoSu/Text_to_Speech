import robot as r

Nam = r.Robot("Nam", "vi")
Lisa = r.Robot("Lisa", "en")

Lisa.RobotRead("I love Tang")
Nam.RobotReadFile("text.txt")
Nam.RobotRead("Tôi đọc có hay không?")
