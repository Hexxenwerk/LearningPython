from paramiko import SSHClient


def main() -> None:
    with SSHClient() as client:
        client.load_system_host_keys()
        client.connect(hostname='ssh-gw.techland.de', username='sysop', port=563, look_for_keys=False)
        stdin, stdout, stderr = client.exec_command('cat .profile')
        print(stdout.read().decode().strip())
        print('Done')
        stdin.close()
        stdout.close()
        stderr.close()
        client.close()


if __name__ == '__main__':
    main()
