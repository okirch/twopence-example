A simple example of how to use twopence

To build a package, use the spec file and extend/adapt to suit your needs.

To simply run on your local machine, try this

 - add your SSH public key to /root/.ssh/authorized_keys
   Note, the key must not be protected with a pass phrase because the
   libssh version currently used by twopence doesn't support this.

 - Then run this in your shell:

	 TWOPENCE_CONFIG_PATH=config
	 ./run

   This should print a few messages documenting the progress of
   the test run.
   When the run is complete, you should find the test report as
   JUnit XML in junit-results.xml

