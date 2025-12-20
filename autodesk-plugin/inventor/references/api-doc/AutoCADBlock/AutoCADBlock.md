# AutoCADBlock Object

## Description

The AutoCADBlock object represents an instance of an AutoCAD block definition on a sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../AutoCADBlock/AutoCADBlock_Delete.md) | Method that deletes the AutoCAD block from the sheet. |
| [GetCustomLineType](../AutoCADBlock/AutoCADBlock_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetPromptTextValues](../AutoCADBlock/AutoCADBlock_GetPromptTextValues.md) | Method that returns the prompt strings and values (attributes) of the block. |
| [GetReferenceKey](../AutoCADBlock/AutoCADBlock_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetCustomLineType](../AutoCADBlock/AutoCADBlock_SetCustomLineType.md) | Method that sets a custom line type to the symbol from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |
| [SetPromptTextValues](../AutoCADBlock/AutoCADBlock_SetPromptTextValues.md) | Method that sets the prompt string values (attributes) of the block. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../AutoCADBlock/AutoCADBlock_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../AutoCADBlock/AutoCADBlock_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Color](../AutoCADBlock/AutoCADBlock_Color.md) | Read-write property that gets and sets the color for the block. Setting the property to Nothing restores the block to the color defined by the layer on which this block resides. |
| [Definition](../AutoCADBlock/AutoCADBlock_Definition.md) | Read-write property that gets and sets the AutoCADBlockDefinition object referenced by the block. |
| [Layer](../AutoCADBlock/AutoCADBlock_Layer.md) | Read-write property that gets and sets the layer associated with the block. |
| [LineType](../AutoCADBlock/AutoCADBlock_LineType.md) | Read-write property that gets and sets the line type override for the block. Setting the property to kDefaultLineType restores the block to the line type defined by the layer on which this block resides. If the property returns kCustomLineType, the GetCustom. |
| [LineWeight](../AutoCADBlock/AutoCADBlock_LineWeight.md) | Read-write property that gets and sets the line weight override for the symbol. Setting the property to 0 restores the symbol to the line weight defined by the layer on which this curve resides. |
| [Name](../AutoCADBlock/AutoCADBlock_Name.md) | Property that indicates the name of this object or instance. |
| [Parent](../AutoCADBlock/AutoCADBlock_Parent.md) | Property that returns the parent Sheet object. |
| [Position](../AutoCADBlock/AutoCADBlock_Position.md) | Read-write property that gets and sets the origin position of the block on the sheet. |
| [Rotation](../AutoCADBlock/AutoCADBlock_Rotation.md) | Read-write property that gets and sets the rotation angle of the block in radians. |
| [Scale](../AutoCADBlock/AutoCADBlock_Scale.md) | Read-write property that gets and sets the scale of the block. |
| [Static](../AutoCADBlock/AutoCADBlock_Static.md) | Read-write property that gets and sets whether to show the scale and rotation grip points on the block. If True, the grip points are disabled. |
| [Transformation](../AutoCADBlock/AutoCADBlock_Transformation.md) | Property that provides the transform that is applied to display the associated AutoCAD block definition in the correct location on the sheet. The matrix defines the sheet to block transform. |
| [Type](../AutoCADBlock/AutoCADBlock_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AutoCADBlocks.Add](../AutoCADBlocks/AutoCADBlocks_Add.md), [AutoCADBlocks.Item](../AutoCADBlocks/AutoCADBlocks_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [AutoCAD block insertion](../../sample-programs/AutoCADBlocks_Add_Sample.md) | Demonstrates inserting an AutoCAD block. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |