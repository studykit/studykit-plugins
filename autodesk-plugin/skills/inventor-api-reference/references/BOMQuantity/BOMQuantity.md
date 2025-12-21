# BOMQuantity Object

## Description

This object provides methods and properties allowing the BOM row unit quantity to be computed.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetBaseQuantity](../BOMQuantity/BOMQuantity_GetBaseQuantity.md) | Method that retrieves the base quantity for the component. |
| [GetEvaluatedBaseQuantity](../BOMQuantity/BOMQuantity_GetEvaluatedBaseQuantity.md) | Method that retrieves the stored base quantity for the component. |
| [SetBaseQuantity](../BOMQuantity/BOMQuantity_SetBaseQuantity.md) | Method that sets the base quantity for the component. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BOMQuantity/BOMQuantity_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BaseUnits](../BOMQuantity/BOMQuantity_BaseUnits.md) | Gets and sets the true unit that the component is quantified in. This property only applies if the BaseQuantity is set to a parameter. |
| [Parent](../BOMQuantity/BOMQuantity_Parent.md) | Property that returns the parent ComponentDefinition object. |
| [Type](../BOMQuantity/BOMQuantity_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnitQuantity](../BOMQuantity/BOMQuantity_UnitQuantity.md) | Property that returns the unit quantity derived from two other properties, the BaseQuantity and the BaseUnits. |

## Accessed From

[AssemblyComponentDefinition.BOMQuantity](../AssemblyComponentDefinition/AssemblyComponentDefinition_BOMQuantity.md), [ComponentDefinition.BOMQuantity](../ComponentDefinition/ComponentDefinition_BOMQuantity.md), [FlatPattern.BOMQuantity](../FlatPattern/FlatPattern_BOMQuantity.md), [PartComponentDefinition.BOMQuantity](../PartComponentDefinition/PartComponentDefinition_BOMQuantity.md), [SheetMetalComponentDefinition.BOMQuantity](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_BOMQuantity.md), [VirtualComponentDefinition.BOMQuantity](../VirtualComponentDefinition/VirtualComponentDefinition_BOMQuantity.md), [WeldmentComponentDefinition.BOMQuantity](../WeldmentComponentDefinition/WeldmentComponentDefinition_BOMQuantity.md), [WeldsComponentDefinition.BOMQuantity](../WeldsComponentDefinition/WeldsComponentDefinition_BOMQuantity.md)

## Version

Introduced in version 10
