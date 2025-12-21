# DrawingPrintManager Object

Derived from: [PrintManager](../PrintManager/PrintManager.md) Object

## Description

The DrawingPrintManager object supports properties and methods that allow you to get and set the printing parameters and submit the print.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetSheetRange](../DrawingPrintManager/DrawingPrintManager_GetSheetRange.md) | Method that gets the sheet range to print. The sheet range is only used when the PrintRange property is set to kPrintSheetRange. |
| [PrintToFile](../DrawingPrintManager/DrawingPrintManager_PrintToFile.md) | Method that prints to the specified file using the current property settings defined by the PrintManager object. |
| [SetCurrentView](../DrawingPrintManager/DrawingPrintManager_SetCurrentView.md) | Set the current view used for printing. |
| [SetSheetRange](../DrawingPrintManager/DrawingPrintManager_SetSheetRange.md) | Method that sets the sheet range to print. The range set is only used when the PrintRange property is set to kPrintSheetRange. |
| [SubmitPrint](../DrawingPrintManager/DrawingPrintManager_SubmitPrint.md) | Method that prints using the current property settings defined by the PrintManager object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AllColorsAsBlack](../DrawingPrintManager/DrawingPrintManager_AllColorsAsBlack.md) | Gets/Sets the Boolean flag indicating whether all the Drawing colors should be black in the print. |
| [Application](../DrawingPrintManager/DrawingPrintManager_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ColorMode](../DrawingPrintManager/DrawingPrintManager_ColorMode.md) | Gets/Sets the color mode to be used for printing. Defaults to using kPrintGrayScale. |
| [NumberOfCopies](../DrawingPrintManager/DrawingPrintManager_NumberOfCopies.md) | Gets/Sets the number of copies to be printed. Defaults to 1. |
| [Orientation](../DrawingPrintManager/DrawingPrintManager_Orientation.md) | Gets/Sets the orientation of the printer. Defaults to the printer's default. |
| [PaperHeight](../DrawingPrintManager/DrawingPrintManager_PaperHeight.md) | Gets/Sets the height of the paper to be printed (max value is 327.67cm). Setting this, sets PaperSize to kPaperSizeCustom. |
| [PaperSize](../DrawingPrintManager/DrawingPrintManager_PaperSize.md) | Gets/Sets the size of the paper to be printed. Defaults to the printer's default. |
| [PaperSource](../DrawingPrintManager/DrawingPrintManager_PaperSource.md) | Gets/Sets the paper source (tray) on the printer. This is printer specific. Defaults to printer's default (denoted by -1). |
| [PaperWidth](../DrawingPrintManager/DrawingPrintManager_PaperWidth.md) | Gets/Sets the width of the paper to be printed (max value is 327.67cm). Setting this, sets PaperSize to kPaperSizeCustom. |
| [Printer](../DrawingPrintManager/DrawingPrintManager_Printer.md) | Gets/Sets the name of the printer. This is the printer's identifier. Defaults to default printer for this machine. |
| [PrinterDeviceContext](../DrawingPrintManager/DrawingPrintManager_PrinterDeviceContext.md) | Gets/Sets the printer's device context. |
| [PrintExcludedSheets](../DrawingPrintManager/DrawingPrintManager_PrintExcludedSheets.md) | Gets/Sets the Boolean flag indicating whether excluded sheets (when PrintRange is set to kPrintAllSheets or kPrintSheetRange) should be printed. Defaults to FALSE. |
| [PrintRange](../DrawingPrintManager/DrawingPrintManager_PrintRange.md) | Gets/Sets information about which sheets are to be printed. Defaults to kPrintCurrentSheet. |
| [RemoveLineWeights](../DrawingPrintManager/DrawingPrintManager_RemoveLineWeights.md) | Gets/Sets the Boolean flag indicating whether the Drawing line weights should be removed in the print. |
| [Rotate90Degrees](../DrawingPrintManager/DrawingPrintManager_Rotate90Degrees.md) | Gets/Sets the Boolean flag indicating whether the Drawing should be rotated 90-deg in the print. |
| [Scale](../DrawingPrintManager/DrawingPrintManager_Scale.md) | Gets/Sets the scale of the print. Meaningless when the ScaleMode is not kPrintCustomScale. |
| [ScaleMode](../DrawingPrintManager/DrawingPrintManager_ScaleMode.md) | Gets/Sets the mode by which the scale of the print is defined. Defaults to kPrintBestFitScale. |
| [TilingEnabled](../DrawingPrintManager/DrawingPrintManager_TilingEnabled.md) | Gets/Sets the Boolean flag indicating whether Tiling is enabled during print. |
| [Type](../DrawingPrintManager/DrawingPrintManager_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Printing - All Sheets in Drawing](../../sample-programs/DrawingPrintManager_Sample.md) | This sample demonstrates how to print all sheets in a drawing document and set some of the DrawingPrintManager properties. |
| [Printing - Drawing Print](../../sample-programs/DrawingPrintManager_SetSheetRange_Sample.md) | This sample demonstrates how to print a drawing, setting specifics such as sheet range. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |