# DrawingBOM Object

## Description

The DrawingBOM object represents a locally stored BOM. This is the equivalent of the table displayed when the 'Attach Balloon From List' command in the context menu of a balloon is invoked.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DrawingBOM/DrawingBOM_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DrawingBOMColumns](../DrawingBOM/DrawingBOM_DrawingBOMColumns.md) | Property that gets the DrawingBOMColumns collection object. |
| [DrawingBOMRows](../DrawingBOM/DrawingBOM_DrawingBOMRows.md) | Property that gets the DrawingBOMRows collection object. |
| [Level](../DrawingBOM/DrawingBOM_Level.md) | Property that returns the type of numbering for the BOM. |
| [Parent](../DrawingBOM/DrawingBOM_Parent.md) | Property that returns the parent DrawingDocument object. |
| [ReferencedDocumentDescriptor](../DrawingBOM/DrawingBOM_ReferencedDocumentDescriptor.md) | Property that gets the model document referenced by this DrawingBOM. |
| [Type](../DrawingBOM/DrawingBOM_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DrawingBOMCell.Parent](../DrawingBOMCell/DrawingBOMCell_Parent.md), [DrawingBOMColumn.Parent](../DrawingBOMColumn/DrawingBOMColumn_Parent.md), [DrawingBOMRow.Parent](../DrawingBOMRow/DrawingBOMRow_Parent.md), [DrawingBOMs.Item](../DrawingBOMs/DrawingBOMs_Item.md)

## Version

Introduced in version 2009
