# SheetFormat Object

## Description

The SheetFormat object represents a sheet format in a drawing.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CopyTo](../SheetFormat/SheetFormat_CopyTo.md) | Method that copies the sheet format to the target drawing document. |
| [Delete](../SheetFormat/SheetFormat_Delete.md) | Method that deletes the sheet format. |
| [GetReferenceKey](../SheetFormat/SheetFormat_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SheetFormat/SheetFormat_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SheetFormat/SheetFormat_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [FitViewsToSheet](../SheetFormat/SheetFormat_FitViewsToSheet.md) | Returns whether to fit the drawing views to the sheet or no. |
| [HasDrawingViews](../SheetFormat/SheetFormat_HasDrawingViews.md) | Property that returns whether this sheet format contains definitions for one or more drawing views. |
| [Height](../SheetFormat/SheetFormat_Height.md) | Property that gets the height of the sheet as defined in the format. |
| [Name](../SheetFormat/SheetFormat_Name.md) | Gets and sets the name of the SheetFormat. |
| [Orientation](../SheetFormat/SheetFormat_Orientation.md) | Property that gets whether the sheet is oriented using landscape or portrait orientation. |
| [Parent](../SheetFormat/SheetFormat_Parent.md) | Property that returns the parent DrawingDocument object. |
| [ReferencedAutoCADBlockDefinitions](../SheetFormat/SheetFormat_ReferencedAutoCADBlockDefinitions.md) | Property that returns an enumerator of all the AutoCADBlockDefinition objects that this format references. The property returns Nothing if the sheet format does not reference any AutoCAD block definitions. |
| [ReferencedBorderDefinition](../SheetFormat/SheetFormat_ReferencedBorderDefinition.md) | Property that returns the BorderDefinition that this format references. |
| [ReferencedSymbolDefinitions](../SheetFormat/SheetFormat_ReferencedSymbolDefinitions.md) | Property that returns an enumerator of all the SketchedSymbolDefinition objects that this format references. |
| [ReferencedTitleBlockDefinition](../SheetFormat/SheetFormat_ReferencedTitleBlockDefinition.md) | Property that returns the TitleBlockDefinition that this format references. |
| [Size](../SheetFormat/SheetFormat_Size.md) | Property that gets the size of the sheet as defined in the format. |
| [TitleBlockLocation](../SheetFormat/SheetFormat_TitleBlockLocation.md) | Property that returns the position of the title block on the sheet as defined in the format. |
| [Type](../SheetFormat/SheetFormat_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Width](../SheetFormat/SheetFormat_Width.md) | Property that gets the width of the sheet as defined in the format. |

## Accessed From

[SheetFormat.CopyTo](../SheetFormat/SheetFormat_CopyTo.md), [SheetFormats.Add](../SheetFormats/SheetFormats_Add.md), [SheetFormats.AddWithOptions](../SheetFormats/SheetFormats_AddWithOptions.md), [SheetFormats.Item](../SheetFormats/SheetFormats_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet with multiple views](../../sample-programs/SheetFormat_Sample.md) | This sample demonstrates the creation of a drawing sheet based on a particular sheet format containing the definition for multiple views. |

## Version

Introduced in version 2009
