# AssetLibraries.MigrateInventorStyle Method

Parent Object: [AssetLibraries](../AssetLibraries/AssetLibraries.md)

## Description

Method that migrates existing inventor color and material styles into an existing or new library.

## Remarks

Color styles are always be imported but you can specify whether to import material styles or not.

## Syntax

AssetLibraries.**MigrateInventorStyle**( ***InventorLibraryPath*** As String, ***ImportMaterialStyles*** As Boolean, ***TargetLibrary*** As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| InventorLibraryPath | String | The full path to the existing Inventor styles. |
| ImportMaterialStyles | Boolean | Indicates if material styles should be imported. |
| TargetLibrary | String | The full path of the library to import the styles into. If the specified library already exists they will be merged into that library. If it doesn’t exist, a new library will be created. |

## Version

Introduced in version 2014
