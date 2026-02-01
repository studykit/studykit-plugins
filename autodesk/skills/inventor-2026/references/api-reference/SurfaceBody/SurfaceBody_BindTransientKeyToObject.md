# SurfaceBody.BindTransientKeyToObject Method

Parent Object: [SurfaceBody](../SurfaceBody/SurfaceBody.md)

## Description

Bind the transient key of a subentity on this body to a live object.

## Syntax

SurfaceBody.**BindTransientKeyToObject**( ***TransientKey*** As Long ) As Object

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TransientKey | Long | Transient key to bind. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Body Imprinting and matching the results](../../sample-programs/ImprintingAndMatching_Sample.md) | This sample is intended to demonstrate a technique of finding the matching surfaces between the original input bodies and output imprinted bodies. This relies on transient keys, which is a unique ID associated with each B-Rep entity. A transient key is only good as long as the model is not recomputed. |

## Version

Introduced in version 9
