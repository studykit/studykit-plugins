# Weld Object

## Description

The Weld object represents a weld within an assembly. The Weld object is a base class of the CosmeticWeld and WeldBead objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../Weld/Weld_Delete.md) | Method that deletes the weld. The arguments allow control over which dependent objects are also deleted. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Weld/Weld_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Name](../Weld/Weld_Name.md) | Gets and sets the name of the Weld. |
| [SymbolAttachPoint](../Weld/Weld_SymbolAttachPoint.md) | Property that returns the coordinate where the weld symbol attached to the weld geometry. |
| [SymbolBreakPoint](../Weld/Weld_SymbolBreakPoint.md) | Property that returns the coordinate where the weld symbol leader line break point is. |
| [Type](../Weld/Weld_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [WeldInfo](../Weld/Weld_WeldInfo.md) | Gets the weld description information as a String containing XML formatted data. For more information on XML formatting see [More XML Weld Info...](MoreXMLWeldInfo_Overview.md) |

## Accessed From

[Welds.Item](../Welds/Welds_Item.md)

## Derived Classes

[CosmeticWeld](../CosmeticWeld/CosmeticWeld.md), [WeldBead](../WeldBead/WeldBead.md)

## Version

Introduced in version 8
