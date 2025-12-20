# PrintManager Object

## Description

The PrintManager object supports properties and methods that allow you to get and set the printing parameters and submit the print job.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [PrintToFile](../PrintManager/PrintManager_PrintToFile.md) | Method that prints to the specified file using the current property settings defined by the PrintManager object. |
| [SetCurrentView](../PrintManager/PrintManager_SetCurrentView.md) | Set the current view used for printing. |
| [SubmitPrint](../PrintManager/PrintManager_SubmitPrint.md) | Method that prints using the current property settings defined by the PrintManager object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PrintManager/PrintManager_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ColorMode](../PrintManager/PrintManager_ColorMode.md) | Gets/Sets the color mode to be used for printing. Defaults to using kPrintGrayScale. |
| [NumberOfCopies](../PrintManager/PrintManager_NumberOfCopies.md) | Gets/Sets the number of copies to be printed. Defaults to 1. |
| [Orientation](../PrintManager/PrintManager_Orientation.md) | Gets/Sets the orientation of the printer. Defaults to the printer's default. |
| [PaperHeight](../PrintManager/PrintManager_PaperHeight.md) | Gets/Sets the height of the paper to be printed (max value is 327.67cm). Setting this, sets PaperSize to kPaperSizeCustom. |
| [PaperSize](../PrintManager/PrintManager_PaperSize.md) | Gets/Sets the size of the paper to be printed. Defaults to the printer's default. |
| [PaperSource](../PrintManager/PrintManager_PaperSource.md) | Gets/Sets the paper source (tray) on the printer. This is printer specific. Defaults to printer's default (denoted by -1). |
| [PaperWidth](../PrintManager/PrintManager_PaperWidth.md) | Gets/Sets the width of the paper to be printed (max value is 327.67cm). Setting this, sets PaperSize to kPaperSizeCustom. |
| [Printer](../PrintManager/PrintManager_Printer.md) | Gets/Sets the name of the printer. This is the printer's identifier. Defaults to default printer for this machine. |
| [PrinterDeviceContext](../PrintManager/PrintManager_PrinterDeviceContext.md) | Gets/Sets the printer's device context. |
| [Type](../PrintManager/PrintManager_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyDocument.PrintManager](../AssemblyDocument/AssemblyDocument_PrintManager.md), [Document.PrintManager](../Document/Document_PrintManager.md), [DrawingDocument.PrintManager](../DrawingDocument/DrawingDocument_PrintManager.md), [PartDocument.PrintManager](../PartDocument/PartDocument_PrintManager.md), [PresentationDocument.PrintManager](../PresentationDocument/PresentationDocument_PrintManager.md)

## Derived Classes

[DrawingPrintManager](../DrawingPrintManager/DrawingPrintManager.md)

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |