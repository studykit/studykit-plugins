# BIMComponentProperty Object

## Description

BIMComponentProperty object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BIMComponentProperty/BIMComponentProperty_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [InternalName](../BIMComponentProperty/BIMComponentProperty_InternalName.md) | Read-only property that gets the internal name of this component property. This name is consistent and can be used as a reliable index for this property. |
| [Name](../BIMComponentProperty/BIMComponentProperty_Name.md) | Read-only property that gets the visible name of this property. This is the name shown to the end-user in the Component Properties list in the Export Building Components dialog. This name is localized and can change for different languages. |
| [Parent](../BIMComponentProperty/BIMComponentProperty_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../BIMComponentProperty/BIMComponentProperty_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Value](../BIMComponentProperty/BIMComponentProperty_Value.md) | Read-write property that gets the value of this BIM property. |

## Accessed From

[BIMComponentPropertySet.Item](../BIMComponentPropertySet/BIMComponentPropertySet_Item.md)

## Version

Introduced in version 2011
