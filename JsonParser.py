import json
from pathlib import Path

scriptDir = Path(__file__).parent

class JsonParser:
    def __init__(self):
        self.dataPath = scriptDir / 'dataset.json'
        self.leaderboardPath = scriptDir / 'leaderboard.json'
        self._validateFile()

    def _validateFile(self):
        with open(self.dataPath, 'r') as file:
            self.dataset = json.load(file)
            self.dataSize = len(self.dataset)

    def getDataSizeByDifficulty(self, difficulty) -> int:
        count = 0
        for data in self.dataset:
            if data["difficulty"] == difficulty:
                count += 1
        return count

    def getStatementAndLogic(self, id: int) -> str:
        for data in self.dataset:
            if data["id"] == id:
                return data["declarativeStatement"], data["logicalConnectives"]

    def getVariablesById(self, id: int) -> list:
        for data in self.dataset:
            if data["id"] == id:
                return data["variables"]

    def getIdsByDifficulty(self, difficulty) -> list:
        ids = []
        for data in self.dataset:
            if data["difficulty"] == difficulty:
                ids.append(data["id"])
        return ids

 
    def storeLeaderboard(self, name, score):
        json_data = {
            'name': name,
            'score': score
        }

        # If file doesnt exists
        if not self.leaderboardPath.exists():
            with open(self.leaderboardPath, 'w') as file:
                json.dump([json_data], file, indent = 4)
            return
        
        # if file does exists
        # load 
        with open(self.leaderboardPath, 'r') as file:
            data = json.load(file)

        # Check if name already exists
        name_found = False
    
        for entry in data:
            if entry["name"].lower() == name.lower():
                entry["score"] += score  # add score
                name_found = True
                break
        # if not found add new 
        if not name_found:
            data.append(json_data)      

        # sort the data from highest to lowest
        data.sort(key=lambda x: x["score"], reverse=True)
        # save it
        with open(self.leaderboardPath, 'w') as file:
            json.dump(data, file, indent = 4)


    def showLeaderboard(self) -> str:
        if not self.leaderboardPath.exists():
            return ""
        
        message = "Leaderboard: \n"

        with open(self.leaderboardPath, 'r') as file:
            datas = json.load(file) 

        for i, data in enumerate(datas, start = 1):
            message += f"{i}. {data['name']} : {data['score']}\n"
        return message





