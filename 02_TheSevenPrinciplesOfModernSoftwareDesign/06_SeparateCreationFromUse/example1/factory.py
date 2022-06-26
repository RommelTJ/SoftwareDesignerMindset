"""
Basic video exporting example
"""

from pathlib import Path
from typing import Protocol, List, Dict, Tuple


def read_choice(question: str, choices: List[str]) -> str:
    choice = ""
    while choice not in choices:
        choice = input(f"{question} ({', '.join(choices)})? ")
    return choice


class VideoExporter(Protocol):
    """Basic representation of a video exporting codec."""

    def prepare_export(self, video_data: str) -> None:
        """Prepares video data for exporting."""
        ...

    def do_export(self, folder: Path) -> None:
        """Exports the video data to a folder."""
        ...


class LosslessVideoExporter:
    def prepare_export(self, video_data: str) -> None:
        print("Preparing video data for lossless export.")

    def do_export(self, folder: Path) -> None:
        print(f"Exporting video data in lossless format to {folder}.")


class H264BPVideoExporter:
    def prepare_export(self, video_data: str) -> None:
        print("Preparing video data for H.264 (Baseline) export.")

    def do_export(self, folder: Path) -> None:
        print(f"Exporting video data in H.264 (Baseline) format to {folder}.")


class H264Hi422PVideoExporter:
    def prepare_export(self, video_data: str) -> None:
        print("Preparing video data for H.264 (Hi422P) export.")

    def do_export(self, folder: Path) -> None:
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}.")


class AudioExporter(Protocol):
    """Basic representation of an audio exporting codec."""

    def prepare_export(self, audio_data: str) -> None:
        """Prepares audio data for exporting."""
        ...

    def do_export(self, folder: Path) -> None:
        """Exports the audio data to a folder."""
        ...


class WAVAudioExporter:
    def prepare_export(self, audio_data: str) -> None:
        print("Preparing audio data for WAV export.")

    def do_export(self, folder: Path) -> None:
        print(f"Exporting audio data in WAV format to {folder}.")


class AACAudioExporter:
    def prepare_export(self, audio_data: str) -> None:
        print("Preparing audio data for AAC export.")

    def do_export(self, folder: Path) -> None:
        print(f"Exporting audio data in AAC format to {folder}.")


class ExporterFactory(Protocol):
    def create_video_exporter(self) -> VideoExporter:
        ...

    def create_audio_exporter(self) -> AudioExporter:
        ...


class LowQualityExporter:
    def create_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()

    def create_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class HighQualityExporter:
    def create_video_exporter(self) -> VideoExporter:
        return H264Hi422PVideoExporter()

    def create_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class MasterQualityExporter:
    def create_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()

    def create_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()


FACTORIES: Dict[str, ExporterFactory] = {
    "low": LowQualityExporter(),
    "high": HighQualityExporter(),
    "master": MasterQualityExporter()
}


def create_exporters() -> Tuple[VideoExporter, AudioExporter]:
    # read the desired export quality
    export_quality = read_choice(
        "What output quality do you want", ["low", "high", "master"]
    )

    factory = FACTORIES[export_quality]
    return factory.create_video_exporter(), factory.create_audio_exporter()


def main() -> None:
    (video_exporter, audio_exporter) = create_exporters()

    # prepare the export
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    # do the export
    folder = Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    main()
