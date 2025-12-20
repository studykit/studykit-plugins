# DesignViewRepresentation.SetSectionView Method

Parent Object: [DesignViewRepresentation](../DesignViewRepresentation/DesignViewRepresentation.md)

## Description

Sets a section view in the design view.

## Syntax

DesignViewRepresentation.**SetSectionView**( ***SectionViewType*** As [SectionViewTypeEnum](../SectionViewTypeEnum.md), [***FirstSectionPlane***] As Variant, [***SecondSectionPlane***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SectionViewType | [SectionViewTypeEnum](../SectionViewTypeEnum.md) | Input SectionViewTypeEnum that specifies the section view type you want to set. |
| FirstSectionPlane | Variant | Optinoal input a Plane object that specifies the first section plane for quarter or three quarter section view and the section plane for the half section view. The normal of the section plane defines the section direction. |
| SecondSectionPlane | Variant | Optinoal input a Plane object that specifies the second section plane for quarter or three quarter section view. The normal of the section plane defines the section direction. If the SectionViewType is not equal to the kQuarterSectionViewType or kThreeQuarterSectionViewType this argument will be ignored.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |