# DesignViewRepresentation.GetSectionViewInfo Method

Parent Object: [DesignViewRepresentation](../DesignViewRepresentation/DesignViewRepresentation.md)

## Description

Gets the current section view info in the design view.

## Syntax

DesignViewRepresentation.**GetSectionViewInfo**( ***SectionViewType*** As [SectionViewTypeEnum](../SectionViewTypeEnum.md), ***FirstSectionPlane*** As [Plane](../Plane/Plane.md), ***SecondSectionPlane*** As [Plane](../Plane/Plane.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SectionViewType | [SectionViewTypeEnum](../SectionViewTypeEnum.md) | Output SectionViewTypeEnum that indicates the current section view type. |
| FirstSectionPlane | [Plane](../Plane/Plane.md) | Output a Plane object that indicates the first section plane for quarter or three quarter section view and the section plane for the half section view. The normal of the section plane indicates the section direction. This returns Nothing if the SectionViewType is equal to kNoSectionViewType. |
| SecondSectionPlane | [Plane](../Plane/Plane.md) | Output a Plane object that indicates the second section plane for quarter or three quarter section view. The normal of the section plane indicates the section direction. This returns Nothing if the SectionViewType is not equal to kQuarterSectionViewType or kThreeQuarterSectionViewType. |

## Version

Introduced in version 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |