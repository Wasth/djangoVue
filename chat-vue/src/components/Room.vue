<template>
    <div id="room">
        <ul>
            <li v-for="room in rooms">
                {{room.creater.username}} - {{room.invited.username}} <br>
                {{room.date}}
            </li>
        </ul>
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Room",
        data(){
            return{
                rooms: ''
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
            });
            this.loadRoom()
        },
        methods:{
            loadRoom(){
                $.ajax({
                    url: this.$store.getters.getVal + 'api/chat/room/',
                    type: 'GET',
                    async: true,
                    success: (response) => {
                        this.rooms = response.data.data
                        console.log(response)
                    }
                })
            }
        }
    }
</script>

<style scoped>

</style>
