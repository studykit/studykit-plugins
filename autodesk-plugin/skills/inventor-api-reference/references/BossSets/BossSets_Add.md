# BossSets.Add Method

Parent Object: [BossSets](../BossSets/BossSets.md)

## Description

Method that creates a new Boss set. The newly created BossSet object is returned.

## Syntax

BossSets.**Add**( ***Centers*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***Type*** As [BossTypeEnum](../BossTypeEnum.md), ***Diameter*** As Variant, ***Offset*** As Variant, ***Taper*** As Variant ) As [BossSet](../BossSet/BossSet.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Centers | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection containing SketchPoint objects that define boss centers. |
| Type | [BossTypeEnum](../BossTypeEnum.md) | Input BossTypeEnum that defines the boss type. This can either be kHeadBossType or kThreadBossType. |
| Diameter | Variant | Input Variant that defines the boss diameter. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| Offset | Variant | Input Variant that defines the offset value. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| Taper | Variant | Input Variant that defines the taper angle for the boss. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |