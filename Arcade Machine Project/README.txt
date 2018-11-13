--------------------------------------------------------------------------
PocketBeagle Arcade Machine
--------------------------------------------------------------------------
License:   
Copyright 2017 Octavo Systems, LLC

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

--------------------------------------------------------------------------

Overview:

  This arcade machine provides two games, Reflex Tester and Simon Says. 
Reflex Tester randomly turns on a button and displays your reaction time once 
you press it. Simon Says generates a button pattern which you have to repeat
to score points. 


Features:

  - Game selection
    - When code begins, choose between games by pressing buttons
	- Pressing Button 0 selects Reflex Tester
	- Pressing Button 1 selects Simon Says
	- Press same button again to confirm or leave to go back 

To Run:

  1) Plug the PocketBeagle microUSB into a power source (either a laptop or 5V USB adapter)
  2) Wait for the PocketBeagle to boot
  4) If you have set the game to auto-run, you're done.  Otherwise,
     move to the directory of the Arcade Machine code.  Run:
        ./run_arcade_machine.sh
