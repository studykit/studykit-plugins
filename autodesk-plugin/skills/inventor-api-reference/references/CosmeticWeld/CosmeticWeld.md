# CosmeticWeld Object

Derived from: [Weld](../Weld/Weld.md) Object

## Description

The CosmeticWeld object represents a cosmetic weld within an assembly. The CosmeticWeld object is derived from the Weld object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../CosmeticWeld/CosmeticWeld_Delete.md) | Method that deletes the weld. The arguments allow control over which dependent objects are also deleted. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CosmeticWeld/CosmeticWeld_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Definition](../CosmeticWeld/CosmeticWeld_Definition.md) | Read-write property that gets and sets the definition object which defines the various inputs that were used to create the cosmetic weld. |
| [Name](../CosmeticWeld/CosmeticWeld_Name.md) | Gets and sets the name of the Weld. |
| [SymbolAttachPoint](../CosmeticWeld/CosmeticWeld_SymbolAttachPoint.md) | Property that returns the coordinate where the weld symbol attached to the weld geometry. |
| [SymbolBreakPoint](../CosmeticWeld/CosmeticWeld_SymbolBreakPoint.md) | Property that returns the coordinate where the weld symbol leader line break point is. |
| [Type](../CosmeticWeld/CosmeticWeld_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [WeldInfo](../CosmeticWeld/CosmeticWeld_WeldInfo.md) | Gets the weld description information as a String containing XML formatted data. For more information on XML formatting see [More XML Weld Info...](MoreXMLWeldInfo_Overview.md) |

## Accessed From

[CosmeticWelds.Add](../CosmeticWelds/CosmeticWelds_Add.md), [CosmeticWelds.Item](../CosmeticWelds/CosmeticWelds_Item.md)

## Version

Introduced in version 8
