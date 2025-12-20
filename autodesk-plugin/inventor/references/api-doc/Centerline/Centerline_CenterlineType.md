# Centerline.CenterlineType Property

Parent Object: [Centerline](../Centerline/Centerline.md)

## Description

Property that gets the centerline type. This could return kRegularCenterline, kBisectorCenterline, kCenteredPatternCenterline or kWorkFeatureCenterline. If the property returns kWorkFeatureCenterline, the centerline is associated with a model work feature. The work feature can be obtained using the ModelWorkFeature property.

## Syntax

Centerline.**CenterlineType**() As [CenterlineTypeEnum](../CenterlineTypeEnum.md)

## Property Value

This is a read only property whose value is a [CenterlineTypeEnum](../CenterlineTypeEnum.md).

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |