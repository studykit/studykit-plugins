# SectionDrawingView.SetAutomatedCenterlineSettings Method

Parent Object: [SectionDrawingView](../SectionDrawingView/SectionDrawingView.md)

## Description

Method that sets the automatic centerline and center mark settings for this view and creates the centerlines and center marks defined by the settings. The centerlines and center marks that were created are returned.

## Syntax

SectionDrawingView.**SetAutomatedCenterlineSettings**( [***AutomatedCenterlineSettings***] As Variant ) As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| AutomatedCenterlineSettings | Variant | Optional input AutomatedCenterlineSettings object that defines the automatic center line and center mark creation settings for this drawing view.  If this argument is omitted the following rules apply. If automated centerlines and center marks have not been created for this view then this argument will default to the settings defined by the drawing settings. If this view has had automatic centerlines and center marks created, then the values used for the previous created are used. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |