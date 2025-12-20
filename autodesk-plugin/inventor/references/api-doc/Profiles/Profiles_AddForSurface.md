# Profiles.AddForSurface Method

Parent Object: [Profiles](../Profiles/Profiles.md)

## Description

Method that creates a profile for creating surface features. The resulting profile could be open or closed.

## Syntax

Profiles.**AddForSurface**( [***Curve***] As Variant ) As [Profile](../Profile/Profile.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Curve | Variant | Optional input sketch curve. The method retrieves the end connected chain of entities that this curve is a part of and creates a profile. If not specified, the method will create a new profile by examining the contents of the sketch and creating a single connected path. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adding a new stitch (knit) feature](../../sample-programs/KnitFeature_Sample.md) | This sample demonstrates the creation of a stitch feature (known as the Knit feature in the API). The sample creates two work surfaces using surface extrusions and stitches them together. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |