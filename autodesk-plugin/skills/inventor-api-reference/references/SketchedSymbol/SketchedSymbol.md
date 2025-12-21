# SketchedSymbol Object

## Description

The SketchedSymbol object represents the instance of a SketchedSymbolDefinition on a sheet. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchedSymbol/SketchedSymbol_Delete.md) | Method that deletes the sketched symbol (e.g. the title block) from the sheet. |
| [GetCustomLineType](../SketchedSymbol/SketchedSymbol_GetCustomLineType.md) | Method that sets a custom line type to the entity from the specified .lin file. The method automatically changes the value of the LineType property to kCustomLineType. |
| [GetReferenceKey](../SketchedSymbol/SketchedSymbol_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetResultText](../SketchedSymbol/SketchedSymbol_GetResultText.md) | Method that returns the text that is currently displayed for a specific text box. This is useful for text boxes that use input form other sources to define their content, i.e. properties and prompted text. The string displayed within this text box is returned. |
| [SetCustomLineType](../SketchedSymbol/SketchedSymbol_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |
| [SetPromptResultText](../SketchedSymbol/SketchedSymbol_SetPromptResultText.md) | Method that sets the text that was supplied for a specified sketched symbol that contains prompted text. The string displayed within this symbol is changed. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchedSymbol/SketchedSymbol_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchedSymbol/SketchedSymbol_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Callout](../SketchedSymbol/SketchedSymbol_Callout.md) | Property that gets whether this sketched symbol is a callout symbol. |
| [Color](../SketchedSymbol/SketchedSymbol_Color.md) | Gets and sets the color for the symbol. |
| [Definition](../SketchedSymbol/SketchedSymbol_Definition.md) | Property returning the sketched symbol definition object referenced by the sketched symbol. |
| [Layer](../SketchedSymbol/SketchedSymbol_Layer.md) | Gets and sets the layer associated with the sketched symbol. |
| [Leader](../SketchedSymbol/SketchedSymbol_Leader.md) | Property that returns the Leader object. |
| [LeaderClipping](../SketchedSymbol/SketchedSymbol_LeaderClipping.md) | Gets and sets whether the symbol's leader should be clipped where it overlaps the symbol. |
| [LeaderStyle](../SketchedSymbol/SketchedSymbol_LeaderStyle.md) | Property that gets and sets the associated leader style. |
| [LeaderVisible](../SketchedSymbol/SketchedSymbol_LeaderVisible.md) | Gets and sets whether the leader of the SketchedSymbol is visible. |
| [LineType](../SketchedSymbol/SketchedSymbol_LineType.md) | Gets and sets the line type override for the symbol. |
| [LineWeight](../SketchedSymbol/SketchedSymbol_LineWeight.md) | Gets and sets the line weight override for the symbol. |
| [Name](../SketchedSymbol/SketchedSymbol_Name.md) | Gets and sets the name of the sketched symbol instance. |
| [Parent](../SketchedSymbol/SketchedSymbol_Parent.md) | Property that gets the parent object from whom this object can logically be reached. |
| [Position](../SketchedSymbol/SketchedSymbol_Position.md) | Gets and sets the origin position of the symbol on the sheet. |
| [Rotation](../SketchedSymbol/SketchedSymbol_Rotation.md) | Gets and sets the rotation angle of the symbol in radians. |
| [Scale](../SketchedSymbol/SketchedSymbol_Scale.md) | Gets and sets the scale of the symbol. |
| [Static](../SketchedSymbol/SketchedSymbol_Static.md) | Gets and sets whether to show the scale and rotation grip points on the SketchedSymbol. |
| [SymbolClipping](../SketchedSymbol/SketchedSymbol_SymbolClipping.md) | Gets and sets whether to trim annotations applied to the SketchedSymbol. |
| [Transformation](../SketchedSymbol/SketchedSymbol_Transformation.md) | Property that provides the transform that is applied to display the associated sketched symbol definition in the correct location on the sheet. The matrix defines the sheet to sketched symbol transform. |
| [Type](../SketchedSymbol/SketchedSymbol_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SketchedSymbols.Add](../SketchedSymbols/SketchedSymbols_Add.md), [SketchedSymbols.AddWithLeader](../SketchedSymbols/SketchedSymbols_AddWithLeader.md), [SketchedSymbols.Item](../SketchedSymbols/SketchedSymbols_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create SketchedSymbol Definition](../../sample-programs/SketchedSymbolDefinition_Sample.md) | This sample illustrates creating a new sketched symbol definition object and inserting it into the active sheet. |
| [Create sketched symbol and leader](../../sample-programs/SketchedSymbols_AddWithLeader_Sample.md) | This sample illustrates creating sketched symbol with a leader. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |