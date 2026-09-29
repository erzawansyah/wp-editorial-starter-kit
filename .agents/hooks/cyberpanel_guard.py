import sys
import json

def main():
    try:
        # Baca payload stdin dari Antigravity Harness
        raw_input = sys.stdin.read()
        if raw_input:
            data = json.loads(raw_input)
            tool_call = data.get("toolCall", {})
            args = tool_call.get("args", {})
            command_line = args.get("CommandLine", "")
            
            # Jika memanggil cyberpanel_provisioner atau perintah server
            if "cyberpanel" in command_line.lower() or "provisioner" in command_line.lower():
                # Tampilkan pengingat di stderr atau respons
                sys.stderr.write("\n[SECURITY AUDIT] Menjalankan operasi server CyberPanel.\n")
    except Exception:
        pass
    
    # PreToolUse output: allow
    output = {
        "decision": "allow"
    }
    sys.stdout.write(json.dumps(output))

if __name__ == "__main__":
    main()
