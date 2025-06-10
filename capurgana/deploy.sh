wait_with_message() {
    local pid=$1
    local message=$2

    local spin='|/-\\'
    local i=0
    while kill -0 "$pid" 2>/dev/null; do
        i=$(( (i + 1) % 4 ))
        printf "\033[32m%c \033[0m%s\r" "${spin:$i:1}" "$message..."
    done
    wait "$pid"
    sleep 1
    echo "----------------------------------------"
    printf "\033[92m✓ \033[0m%s\n\n" "$message.       "
}

cd Maria_Luna_Pages/

git pull origin main & 2>&1
wait_with_message $! "Pulling from main"

source .venv/bin/activate
cd capurgana/___/

python3 manage.py collectstatic --noinput & 2>&1
wait_with_message $! "Collecting Static"

python3 manage.py makemigrations & 2>&1
wait_with_message $! "Making migrations"

python3 manage.py migrate & 2>&1
wait_with_message $! "Migrating"

source ~/.bashrc
python3 manage.py check --deploy & 2>&1
wait_with_message $! "Running 'python3 manage.py check --deploy'"

sudo service capurgana restart & 2>&1
wait_with_message $! "Restarting sapzurro service"

echo "----------------------------------------"
echo -e "\033[92m✓ \033[0mSuccessfully Updated Sapzurro Page.\n "
