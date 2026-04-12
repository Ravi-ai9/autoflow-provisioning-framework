def run(self):
    while self.state != State.DONE:

        try:
            self.logger.info(f"Running: {self.state}")

            # 🔥 mark start
            self.monitor.update(self.state.name, "STARTED")

            if self.state == State.BOOTSTRAP:
                self.state = State.PRECHECK

            elif self.state == State.PRECHECK:
                self.state = State.IFWI

            elif self.state == State.IFWI:
                self.ifwi.run()
                self.state = State.BIOS

            elif self.state == State.BIOS:
                self.bios.run()
                self.state = State.OS

            elif self.state == State.OS:
                self.os.run()
                self.state = State.CLEANUP

            elif self.state == State.CLEANUP:
                self.logger.info("Cleaning up system...")
                self.state = State.DONE

            # 🔥 mark success
            self.monitor.update(self.state.name, "COMPLETED")

            # reset retry on success
            self.retry_count = 0

        except Exception as e:
            self.logger.error(f"Error in {self.state}: {e}")
            self.monitor.update(self.state.name, f"FAILED: {str(e)}")

            self.retry_count += 1

            if self.retry_count < self.max_retry:
                self.logger.info("Retrying...")
            else:
                self.logger.error("Max retries reached. Stopping pipeline.")
                break

    self.logger.info("Pipeline Completed!")
    self.logger.info(f"Final Status: {self.monitor.get_status()}")