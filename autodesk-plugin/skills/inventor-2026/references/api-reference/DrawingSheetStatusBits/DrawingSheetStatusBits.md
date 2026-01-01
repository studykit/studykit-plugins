# DrawingSheetStatusBits Enumerator

## Description

Bits indicating out-of-date status of Drawing Sheet.

## Methods

|  |  |  |
| --- | --- | --- |
| Name | Value | Description |
| kAssyCompositionOutOfDateDrawingSheet | 4 | Assembly on the Sheet has undergone some composition changes. And the Sheet rendition is out-of-date. |
| kAssyPositionOutOfDateDrawingSheet | 2 | Assembly on the Sheet has undergone positional changes. And the Sheet rendition is out-of-date. |
| kGeomOutOfDateDrawingSheet | 1 | Geometric content of a Part on the sheet has changed. And the Sheet rendition is out-of-date. |
| kNoDataDrawingSheet | 128 | Rendition of this Sheet is not available. |
| kParameterizedTextOutOfDateDrawingSheet | 32 | Parameterized Text used on the Sheet has changed. And the Sheet rendition is out-of-date. |
| kProcessingPreciseDisplayDrawingSheet | 256 | Hidden-line display in one or more views is in progress. Sheet may print with incomplete graphical representation. |
| kResourceTemplateOutOfDateDrawingSheet | 16 | Resource Templates used on the Sheet have changed. And the Sheet rendition is out-of-date. |
| kStandardOutOfDateDrawingSheet | 8 | Drafting Standard of the Sheet has changed. And the Sheet rendition is out-of-date. |
| kUnknownOutOfDateDrawingSheet | 64 | Up-to-date status of the rendition of this Sheet could not be fully determined. |
| kUpToDateDrawingSheet | 0 | Check for equality with this enum to see if Sheet is fully up-to-date. |

## Version

Introduced in version 4
