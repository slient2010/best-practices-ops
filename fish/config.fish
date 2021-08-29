# starship init fish | source
helm completion fish | source
export PATH="$HOME/.cargo/bin:$PATH:/usr/share/bcc/tools:/data/work/apps/openresty/bin"
export EDITOR=vim
# export PGPASSWORD="abcd1234!"
export PGPASSWORD="ueKoCha0ou"

# Login from the ssh client, do nothing.
if test ! \( -n "$SSH_CONNECTION" \) 
    if test ! \( -n "$TMUX" \)
        tmux new -As (basename (tty))
    end
end

# if test ! \( -n "$SSH_CONNECTION" \) 
#     if test \( -n "$TMUX" \)
#         tmux >/dev/null 2>&1; 
#     else
#         tmux new -As (basename (tty))
#     end
# end

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
eval /home/jun/.anaconda3/bin/conda "shell.fish" "hook" $argv | source
# <<< conda initialize <<<

alias docker="podman"

# >>> ssh-agent >>>
echo "Checking ssh-agent status, wait for a moment."
# sleep 0.1
set SSH_AGENT_PID (sudo pgrep ssh-agent | head -n 1)
if test ! \( -n "$SSH_AGENT_PID" \)
    set SSH_AUTH_SOCK 
    set SSH_AGENT_PID
    nohup ssh-agent 1>&2  2>/dev/null
    set SSH_AGENT_PID (sudo pgrep ssh-agent | head -n 1)
end

set SSH_AUTH_SOCK (sudo lsof -p "$SSH_AGENT_PID" | grep tmp |  awk '{print $9}' | uniq )
export SSH_AUTH_SOCK;
export SSH_AGENT_PID; 
ssh-add ~/.ssh/id_rsa >/dev/null 2>&1;
ssh-add ~/.ssh/my-mac/id_rsa >/dev/null 2>&1;
# <<< ssh-agent <<<

alias ngx="cd /data/work/apps/openresty/nginx/"
export GOPATH="/data/programing/golang"
