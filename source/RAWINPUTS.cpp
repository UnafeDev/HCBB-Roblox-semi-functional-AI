#include <windows.h>
#include <fstream>
#include <iostream>
#include <string>
#include <chrono>   
#include <thread> 

using namespace std;

void moveMouse(int x, int y) {
    INPUT input = {0};
    input.type = INPUT_MOUSE;
    input.mi.dwFlags = MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE;
    input.mi.dx = x * 65535 / GetSystemMetrics(SM_CXSCREEN);
    input.mi.dy = y * 65535 / GetSystemMetrics(SM_CYSCREEN);
    SendInput(1, &input, sizeof(INPUT));
}

int main() {
    const string coordFile = "coords.txt";

    cout << "Starting mouse mover... Monitoring " << coordFile << "\n";

    while (true) {
        ifstream infile(coordFile);
        int x, y;

        if (infile >> x >> y) {
            cout << "Read coordinates: (" << x << ", " << y << ")\n";
            moveMouse(x, y);
        } else {
            cout << "No valid coordinates found in file.\n";
        }

        infile.close();
        this_thread::sleep_for(chrono::milliseconds(10));
    }

    return 0;
}
