const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const { exec } = require("child_process");

const app = express();
app.use(cors());
app.use(bodyParser.json());

// Open CMD on your system
app.post("/open-cmd", (req, res) => {
  exec("start cmd.exe", (error, stdout, stderr) => {
    if (error) {
      return res.json({ output: stderr || error.message });
    }
    res.json({ output: "CMD Opened Successfully!" });
  });
});

// Execute normal system commands
app.post("/cmd", (req, res) => {
  let { command } = req.body;

  // If it's an SSH command, replace with plink syntax
  if (command.startsWith("ssh ")) {
    const args = command.split(" ");
    const userHost = args[1]; // user@ip
    const remoteCmd = args.slice(2).join(" ") || "ls";

    const password = "yourPassword"; // optional for key auth
    command = `plink -ssh ${userHost} -pw ${password} "${remoteCmd}"`;
  }

  exec(command, { shell: "cmd.exe" }, (error, stdout, stderr) => {
    if (error) {
      return res.json({ output: stderr || error.message });
    }
    res.json({ output: stdout });
  });
});

app.listen(3000, () => {
  console.log("📟 CMD server is running on http://localhost:3000");
});
