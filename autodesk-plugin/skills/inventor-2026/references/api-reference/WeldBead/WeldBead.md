# WeldBead Object

Derived from: [Weld](../Weld/Weld.md) Object

## Description

The WeldBead object represents a weld bead within an assembly. The WeldBead object is derived from the Weld object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../WeldBead/WeldBead_Delete.md) | Method that deletes the weld. The arguments allow control over which dependent objects are also deleted. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../WeldBead/WeldBead_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BeadFaces](../WeldBead/WeldBead_BeadFaces.md) | Property that returns the set of  that define the geometric result of the weld bead. |
| [BeadLength](../WeldBead/WeldBead_BeadLength.md) | Gets the length of the weld bead. |
| [EndFaces](../WeldBead/WeldBead_EndFaces.md) | Gets the set of faces that define the ends of the weld bead. |
| [FaceSetOne](../WeldBead/WeldBead_FaceSetOne.md) | Returns the first set of faces the weld bead is on. |
| [FaceSetTwo](../WeldBead/WeldBead_FaceSetTwo.md) | Returns the second set of faces the weld bead is on. |
| [Name](../WeldBead/WeldBead_Name.md) | Gets and sets the name of the Weld. |
| [SideFaces](../WeldBead/WeldBead_SideFaces.md) | Gets the set of faces that define the sides of the weld bead. |
| [SymbolAttachPoint](../WeldBead/WeldBead_SymbolAttachPoint.md) | Property that returns the coordinate where the weld symbol attached to the weld geometry. |
| [SymbolBreakPoint](../WeldBead/WeldBead_SymbolBreakPoint.md) | Property that returns the coordinate where the weld symbol leader line break point is. |
| [Type](../WeldBead/WeldBead_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [WeldInfo](../WeldBead/WeldBead_WeldInfo.md) | Gets the weld description information as a String containing XML formatted data. For more information on XML formatting see [More XML Weld Info...](MoreXMLWeldInfo_Overview.md) |

## Accessed From

[WeldBeads.Item](../WeldBeads/WeldBeads_Item.md)

## Version

Introduced in version 8
