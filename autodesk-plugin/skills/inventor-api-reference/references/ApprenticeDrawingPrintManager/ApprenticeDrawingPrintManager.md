# ApprenticeDrawingPrintManager Object

Derived from: [ApprenticePrintManager](../ApprenticePrintManager/ApprenticePrintManager.md) Object

## Description

The ApprenticeDrawingPrintManager object supports properties and methods that allow you to get and set the printing parameters and submit the print job.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetSheetRange](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager_GetSheetRange.md) | Method that gets the sheet range to print. The sheet range is only used when the PrintRange property is set to kPrintSheetRange. |
| [PrintToFile](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager_PrintToFile.md) | Method that prints to the specified file using the current property settings defined by the ApprenticePrintManager object. |
| [SetCurrentView](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager_SetCurrentView.md) | Property to set the current view, to be used for printing. |
| [SetSheetRange](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager_SetSheetRange.md) | Property to indicate the range of Sheets to be printed. Valid only when PrintRange is set to kPrintSheetRange. |
| [SubmitPrint](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager_SubmitPrint.md) | Method that prints using the current property settings defined by the ApprenticePrintManager object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AllColorsAsBlack](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager_AllColorsAsBlack.md) | Gets/Sets the Boolean flag indicating whether all the Drawing colors should be black in the print. |
| [ColorMode](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager_ColorMode.md) | Gets/Sets the color mode to be used for printing. Defaults to using kPrintGrayScale. |
| [NumberOfCopies](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager_NumberOfCopies.md) | Gets/Sets the number of copies to be printed. Defaults to 1. |
| [Orientation](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager_Orientation.md) | Gets/Sets the orientation of the printer. Defaults to the printer's default. |
| [PaperHeight](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager_PaperHeight.md) | Gets/Sets the height of the paper to be printed. Setting this, sets PaperSize to kPaperSizeCustom. |
| [PaperSize](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager_PaperSize.md) | Gets/Sets the size of the paper to be printed. Defaults to the printer's default. |
| [PaperSource](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager_PaperSource.md) | Gets/Sets the paper source (tray) on the printer. This is printer specific. Defaults to printer's default (denoted by -1). |
| [PaperWidth](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager_PaperWidth.md) | Gets/Sets the width of the paper to be printed. Setting this, sets PaperSize to kPaperSizeCustom. |
| [Printer](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager_Printer.md) | Gets/Sets the name of the printer. This is the printer's identifier. Defaults to default printer for this machine. |
| [PrinterDeviceContext](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager_PrinterDeviceContext.md) | Gets/Sets the printer's device context. |
| [PrintExcludedSheets](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager_PrintExcludedSheets.md) | Gets/Sets the Boolean flag indicating whether excluded sheets (when PrintRange is set to kPrintAllSheets or kPrintSheetRange) should be printed. Defaults to FALSE. |
| [PrintRange](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager_PrintRange.md) | Gets/Sets information about which sheets are to be printed. Defaults to kPrintCurrentSheet. |
| [RemoveLineWeights](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager_RemoveLineWeights.md) | Gets/Sets the Boolean flag indicating whether the Drawing line weights should be removed in the print. |
| [Rotate90Degrees](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager_Rotate90Degrees.md) | Gets/Sets the Boolean flag indicating whether the Drawing should be rotated 90-deg in the print. |
| [Scale](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager_Scale.md) | Gets/Sets the scale of the print. Meaningless when the ScaleMode is not kPrintCustomScale. |
| [ScaleMode](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager_ScaleMode.md) | Gets/Sets the mode by which the scale of the print is defined. Defaults to kPrintBestFitScale. |
| [Type](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |