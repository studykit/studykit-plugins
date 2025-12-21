# ApprenticePrintManager Object

## Description

The ApprenticePrintManager object supports properties and methods that allow you to get and set the printing parameters and submit the print job.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [PrintToFile](../ApprenticePrintManager/ApprenticePrintManager_PrintToFile.md) | Method that prints to the specified file using the current property settings defined by the ApprenticePrintManager object. |
| [SetCurrentView](../ApprenticePrintManager/ApprenticePrintManager_SetCurrentView.md) | Property to set the current view, to be used for printing. |
| [SubmitPrint](../ApprenticePrintManager/ApprenticePrintManager_SubmitPrint.md) | Method that prints using the current property settings defined by the ApprenticePrintManager object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ColorMode](../ApprenticePrintManager/ApprenticePrintManager_ColorMode.md) | Gets/Sets the color mode to be used for printing. Defaults to using kPrintGrayScale. |
| [NumberOfCopies](../ApprenticePrintManager/ApprenticePrintManager_NumberOfCopies.md) | Gets/Sets the number of copies to be printed. Defaults to 1. |
| [Orientation](../ApprenticePrintManager/ApprenticePrintManager_Orientation.md) | Gets/Sets the orientation of the printer. Defaults to the printer's default. |
| [PaperHeight](../ApprenticePrintManager/ApprenticePrintManager_PaperHeight.md) | Gets/Sets the height of the paper to be printed. Setting this, sets PaperSize to kPaperSizeCustom. |
| [PaperSize](../ApprenticePrintManager/ApprenticePrintManager_PaperSize.md) | Gets/Sets the size of the paper to be printed. Defaults to the printer's default. |
| [PaperSource](../ApprenticePrintManager/ApprenticePrintManager_PaperSource.md) | Gets/Sets the paper source (tray) on the printer. This is printer specific. Defaults to printer's default (denoted by -1). |
| [PaperWidth](../ApprenticePrintManager/ApprenticePrintManager_PaperWidth.md) | Gets/Sets the width of the paper to be printed. Setting this, sets PaperSize to kPaperSizeCustom. |
| [Printer](../ApprenticePrintManager/ApprenticePrintManager_Printer.md) | Gets/Sets the name of the printer. This is the printer's identifier. Defaults to default printer for this machine. |
| [PrinterDeviceContext](../ApprenticePrintManager/ApprenticePrintManager_PrinterDeviceContext.md) | Gets/Sets the printer's device context. |
| [Type](../ApprenticePrintManager/ApprenticePrintManager_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ApprenticeServerDocument.PrintManager](../ApprenticeServerDocument/ApprenticeServerDocument_PrintManager.md), [ApprenticeServerDrawingDocument.PrintManager](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_PrintManager.md)

## Derived Classes

[ApprenticeDrawingPrintManager](../ApprenticeDrawingPrintManager/ApprenticeDrawingPrintManager.md)

## Version

Introduced in version 9
