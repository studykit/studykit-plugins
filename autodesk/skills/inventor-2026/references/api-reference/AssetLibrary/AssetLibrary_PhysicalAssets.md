# AssetLibrary.PhysicalAssets Property

Parent Object: [AssetLibrary](../AssetLibrary/AssetLibrary.md)

## Description

Gets an Assets collection which provides access to all of the physical assets in this library. A physical asset defines the physical properties that are associated with a material.

## Syntax

AssetLibrary.**PhysicalAssets**() As [AssetsEnumerator](../AssetsEnumerator/AssetsEnumerator.md)

## Property Value

This is a read only property whose value is an [AssetsEnumerator](../AssetsEnumerator/AssetsEnumerator.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Write out all physical properties to a file.](../../sample-programs/DumpAllPhysicalProperties_Sample.md) | This sample writes out information about all of the physical properties in all libraries. This can be useful when trying to use the API to modify existing materials by allowing to easily see what information is available for a physical property. |

## Version

Introduced in version 2014
