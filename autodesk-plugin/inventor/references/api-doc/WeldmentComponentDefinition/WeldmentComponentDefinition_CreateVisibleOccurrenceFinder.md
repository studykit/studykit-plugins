# WeldmentComponentDefinition.CreateVisibleOccurrenceFinder Method

Parent Object: [WeldmentComponentDefinition](../WeldmentComponentDefinition/WeldmentComponentDefinition.md)

## Description

Method that creates an occurrence finder object that allows you to find all occurrences that are visible or hidden by a defined amount. By default, visible is defined by a portion of the part being visible from any view of the part. Optionally you can specify a camera to limit the viewing angle and the extents.

## Syntax

WeldmentComponentDefinition.**CreateVisibleOccurrenceFinder**( ***Visible*** As Boolean, ***PercentageVisible*** As Double, ***Compact*** As Boolean ) As [VisibleOccurrenceFinder](../VisibleOccurrenceFinder/VisibleOccurrenceFinder.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Visible | Boolean | Input Boolean that defines if visible or hidden objects should be found. If True then fully and partially visible occurrences will be returned. If False, completely and partially hidden occurrences will be returned. |
| PercentageVisible | Double | Input Double that defines the percentage of the component that can be visible or hidden. A value of 1 (100%) indicates that all components that are visible at all, or that are completely hidden (depending on the Visible argument) will be returned. A value of 0 (0%) indicates that the most visible or hidden components will be returned. |
| Compact | Boolean | Input Boolean that defines if all components that are found within an assembly will be consolidated so that their parent assembly is returned instead of each one of the child components. A value of True indicates that they will be consolidated. |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |