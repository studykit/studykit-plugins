# FinishFeatures.CreateDefinition Method

Parent Object: [FinishFeatures](../FinishFeatures/FinishFeatures.md)

## Description

Method that creates a new FinishDefinition object. The object created does not represent a finish feature but instead is a representation of the information that defines a finish feature. You can use this object as input to the FinishFeatures.Add method to cre.

## Syntax

FinishFeatures.**CreateDefinition**( ***pIncludedEntities*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***vtExcludedEntities***] As Variant, [***FinishType***] As [FinishTypeEnum](../FinishTypeEnum.md), [***vtProcessName***] As Variant, [***vtAppearance***] As Variant, [***vtMoreOptions***] As Variant ) As [FinishDefinition](../FinishDefinition/FinishDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| pIncludedEntities | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection that specifies the Face and SurfaceBody objects and their proxies on which the finish feature is created. Valid objects in the ObjectCollection can be Face, SurfaceBody and the proxies, or FaceCollection that contains Face or FaceProxy objects |
| vtExcludedEntities | Variant | Input ObjectCollection that specifies the Face objects and their proxies that will be excluded from the finish feature. Valid objects in the ObjectCollection can be Face objects and the proxies. |
| FinishType | [FinishTypeEnum](../FinishTypeEnum.md) | Optional input FinishTypeEnum value that specifies finish type. If not provided the default kAppearanceFinishType will be used.   This is an optional argument whose default value is 124929. |
| vtProcessName | Variant | Optional input String value that specifies finish process name.   This is an optional argument whose default value is null. |
| vtAppearance | Variant | Optional input Asset object that specifies finish appearance.   This is an optional argument whose default value is null. |
| vtMoreOptions | Variant | Optional input NameValueMap that specifies more options. This is for future use.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2025.1
