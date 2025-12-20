# SectionDrawingView.DrawingCurves Property

Parent Object: [SectionDrawingView](../SectionDrawingView/SectionDrawingView.md)

## Description

Property that returns all the drawing curves within the drawing view optionally filtered to the input model object. This property returns Nothing for draft views.iew object represents a drawing view on a sheet.

## Syntax

SectionDrawingView.**DrawingCurves**( [***ModelObject***] As Variant ) As [DrawingCurvesEnumerator](../DrawingCurvesEnumerator/DrawingCurvesEnumerator.md)

## Property Value

This is a read only property whose value is a [DrawingCurvesEnumerator](../DrawingCurvesEnumerator/DrawingCurvesEnumerator.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ModelObject | Variant | Optional input object that specifies the object from the model for which the corresponding drawing view curves need to be retrieved. This could be an Edge, Face, PartFeature, Sketch, SketchEntity, Sketch3D, SketchEntity3D, ComponentOccurrence, or the proxies to any of these. If not specified, all the edges from the drawing view are returned. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |