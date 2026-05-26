import { DashboardShell } from "@/components/DashboardShell";
import {
  alerts,
  cases,
  fillableTabs,
  metrics,
  protocolHighlights,
  reportSections,
  skillDomains
} from "@/lib/mock-data";

export default function Home() {
  return (
    <DashboardShell
      alerts={alerts}
      cases={cases}
      fillableTabs={fillableTabs}
      metrics={metrics}
      protocolHighlights={protocolHighlights}
      reportSections={reportSections}
      skillDomains={skillDomains}
    />
  );
}
