# OccurrencePatterns.AddFeatureBasedPattern Method

Parent Object: [OccurrencePatterns](../OccurrencePatterns/OccurrencePatterns.md)

## Description

Method that creates a new occurrence pattern of the input component(s) using a pattern feature to define the positions of the elements within the pattern.

## Syntax

OccurrencePatterns.**AddFeatureBasedPattern**( ***ParentComponents*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***FeaturePattern*** As [PartFeature](../PartFeature/PartFeature.md) ) As [FeatureBasedOccurrencePattern](../FeatureBasedOccurrencePattern/FeatureBasedOccurrencePattern.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ParentComponents | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection that contains the components to pattern. The valid objects that can be specified in the collection are ComponentOccurrence and OccurrencePattern objects. |
| FeaturePattern | [PartFeature](../PartFeature/PartFeature.md) | Input PatternFeatureProxy object that defines which pattern feature to use for this occurrence pattern. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |