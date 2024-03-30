# server update 
echo 'start: server update'
cp -r ../html ../..
mv ../../html/index.html ../..
cp -r ../images ../..
cp -r ../css ../..
cp ../sitemap.xml ../..
echo 'cp -r ../html ../..'
echo 'mv ../../html/index.html ../..'
echo 'cp -r ../images ../..'
echo 'cp -r ../css ../..'
echo 'cp ../sitemap.xml ../..'
echo 'finish: server update'
