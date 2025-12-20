# BorderDefinition Object

## Description

The BorderDefinition object represents a border definition.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CopyTo](../BorderDefinition/BorderDefinition_CopyTo.md) | Method that copies the definition to the target drawing document. |
| [Delete](../BorderDefinition/BorderDefinition_Delete.md) | Method that deletes the BorderDefinition object. This method will fail in the case where the definition is being referenced. This can be determined by using the IsReferenced property. |
| [Edit](../BorderDefinition/BorderDefinition_Edit.md) | Method that opens a copy of the border definition's sketch for edit in the Sketch environment. |
| [ExitEdit](../BorderDefinition/BorderDefinition_ExitEdit.md) | Method that closes the currently active sketch (see below for limitations) and depending on the input parameters, replaces the sketch of the border definition with the edited sketch. |
| [GetReferenceKey](../BorderDefinition/BorderDefinition_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BorderDefinition/BorderDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../BorderDefinition/BorderDefinition_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [IsDefault](../BorderDefinition/BorderDefinition_IsDefault.md) | Gets if the border definition is default or not. |
| [IsReferenced](../BorderDefinition/BorderDefinition_IsReferenced.md) | Property that specifies if the border definition is being referenced or not. A border definition is referenced whenever it is used on a sheet. A referenced border definition cannot be deleted. |
| [Name](../BorderDefinition/BorderDefinition_Name.md) | Gets and sets the name of the border definition. |
| [Parent](../BorderDefinition/BorderDefinition_Parent.md) | Property returning the parent . |
| [Sketch](../BorderDefinition/BorderDefinition_Sketch.md) | Property that returns the sketch associated with the border definition. The DrawingSketch returned by the Sketch property supports all query functionality but cannot be edited. To edit the contents of a border definition, use the Edit method. This creates a copy of the border definition's sketch for edit. The ExitEdit method of the BorderDefinition can then be used to save the edited sketch as the border definition's sketch. |
| [Type](../BorderDefinition/BorderDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Border.Definition](../Border/Border_Definition.md), [BorderDefinition.CopyTo](../BorderDefinition/BorderDefinition_CopyTo.md), [BorderDefinitions.Add](../BorderDefinitions/BorderDefinitions_Add.md), [BorderDefinitions.Item](../BorderDefinitions/BorderDefinitions_Item.md), [DefaultBorder.Definition](../DefaultBorder/DefaultBorder_Definition.md), [SheetFormat.ReferencedBorderDefinition](../SheetFormat/SheetFormat_ReferencedBorderDefinition.md)

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |