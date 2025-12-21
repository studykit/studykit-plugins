# SurfaceBody.RangeBox Property

Parent Object: [SurfaceBody](../SurfaceBody/SurfaceBody.md)

## Description

Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object.

## Syntax

SurfaceBody.**RangeBox**() As [Box](../Box/Box.md)

## Property Value

This is a read only property whose value is a [Box](../Box/Box.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client Graphics - Vertex Color by Z Height](../../sample-programs/GraphicsDataSets_CreateColorSet_Sample.md) | This sample demonstrates using client graphics and some other functions that help to support display control. It uses the currently active part and replaces the part display with a display where the part's color varies from blue to red where blue is assigned to the lowest Z portion of the part and red is assigned to the highest Z portion of the part. Areas in between are represented by a smooth blend of color from blue to red. |
| [Body Imprinting and matching the results](../../sample-programs/ImprintingAndMatching_Sample.md) | This sample is intended to demonstrate a technique of finding the matching surfaces between the original input bodies and output imprinted bodies. This relies on transient keys, which is a unique ID associated with each B-Rep entity. A transient key is only good as long as the model is not recomputed. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |